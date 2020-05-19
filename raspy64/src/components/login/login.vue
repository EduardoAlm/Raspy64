<template>
  <v-container>
    <v-layout row wrap>
      <v-flex>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>

          <v-text-field
            v-model="password"
            :rules="passwordRules"
            label="Password"
            required
            :append-icon="passwordShow ? 'visibility' : 'visibility_off'"
            :type="passwordShow ? 'text' : 'password'"
            @click:append="passwordShow = !passwordShow"
          ></v-text-field>

          <v-alert type="info">
            After u click on the button below you will recieve an sms with a
            verification code.
          </v-alert>

          <v-btn :disabled="!valid" class="mx-2" color="success" @click="validate">Get Sign In Code</v-btn>
          <v-btn class="mx-2" color="error" @click="reset">Reset Form</v-btn>
        </v-form>
      </v-flex>
    </v-layout>
    <div v-if="success">
      <v-form>
        <div class="form-group">
          <v-text-field v-model="code" label="Verification Code" required />
        </div>
        <div v-if="success">
          <v-btn class="mx-2" color="success" @click="finalCode(code)">Log In</v-btn>
        </div>
      </v-form>
    </div>
    <div id="recaptcha"></div>
  </v-container>
</template>

<script>
import * as firebase from "firebase";
import cryptico from "cryptico";
export default {
  data: () => ({
    passwordShow: false,
    valid: true,
    email: "",
    success: false,
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    password: "",
    passwordRules: [v => !!v || "Password is Required"],
    code: "",
    result: "",
    login: false
  }),
  methods: {
    async loginWithFirebase(user) {
      await this.$store.dispatch("signInActionEmail", user);
      if (this.$store.state.statusEmail == "success") {
        const appVerifier = window.recaptchaVerifier;
        this.smssignin(appVerifier);
      }
    },
    async smssignin(appVerifier) {
      var phonenumber = "";
      const RSAkeys = cryptico.generateRSAKey("WeLoveInacio", 2048);
      await firebase
        .database()
        .ref("/Users/" + this.$store.state.user)
        .once("value")
        .then(function(snapshot) {
          phonenumber =
            cryptico.decrypt(
              snapshot.val() && snapshot.val().phonenumber,
              RSAkeys
            ).plaintext || "Anonymous";
        });

      await firebase
        .auth()
        .signInWithPhoneNumber(phonenumber, appVerifier)
        .then(response => {
          // success
          this.success = true;
          window.response = response;
          this.result = response;
          alert("success");
        })
        .catch(() => {
          alert("Failure");
        });
    },
    async finalCode() {
      var code = this.code;
      var login = false;
      await this.result
        .confirm(code)
        .then(function() {
          // User signed in successfully.
          //var user = result.user;
          login = "true";
          alert("success");

          // ...
        })
        .catch(function() {
          // User couldn't sign in (bad verification code?)
          // ...
          alert("failure");
        });

      if (login == "true") {
        this.$store.dispatch("updateloggedIn");
      }
    },
    async validate() {
      if (this.$refs.form.validate()) {
        const user = {
          email: this.email,
          password: this.password
        };
        this.loginWithFirebase(user);
      }
    },
    reset() {
      this.$refs.form.reset();
    }
  },
  mounted() {
    window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier(
      "recaptcha",
      {
        size: "normal",
        callback: function(response) {
          // reCAPTCHA solved, allow signInWithPhoneNumber.
          // ...
          console.log("success", response);
        },
        "expired-callback": function() {
          // Response expired. Ask user to solve reCAPTCHA again.
          // ...
        }
      }
    );
    window.recaptchaVerifier.render().then(widgetId => {
      window.recaptchaWidgetId = widgetId;
    });
  }
};
</script>
