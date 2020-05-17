<template>
  <v-container>
    <v-layout row wrap>
      <v-flex>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>

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

          <v-btn
            :disabled="!valid"
            class="mx-2"
            color="success"
            @click="validate"
            >Get Sign In Code</v-btn
          >
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
          <v-btn class="mx-2" color="success" @click="loginWithFirebase"
            >Log In</v-btn
          >
        </div>
      </v-form>
    </div>
    <div id="recaptcha"></div>
  </v-container>
</template>

<script>
import * as firebase from "firebase";
export default {
  data: () => ({
    passwordShow: false,
    valid: true,
    email: "",
    success: false,
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
    ],
    password: "",
    phonenumber: "",
    passwordRules: [(v) => !!v || "Password is Required"],
    code: "",
    result: "",
    login: true,
  }),
  methods: {
    async validate() {
      if (this.$refs.form.validate()) {
        const phone = this.$store.dispatch("get_userphone");
        const appVerifier = window.recaptchaVerifier;
        firebase
          .auth()
          .signInWithPhoneNumber(this.phonenumber, appVerifier)
          .then((response) => {
            // success
            this.success = true;
            console.log("success", response);
            this.result = response;
            window.response = response;
          })
          .catch(() => {
            // error
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    loginWithFirebase() {
      const user = {
        email: this.email,
        password: this.password,
      };

      this.result
        .confirm(this.code)
        .then(function(result) {
          // User signed in successfully.
          //var user = result.user;

          console.log(result);

          // ...
        })
        .catch(function(error) {
          // User couldn't sign in (bad verification code?)
          // ...
          this.login = false;
          console.log(error);
        });
      if (this.login) {
        this.$store.dispatch("signInAction", user);
      }
    },
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
        },
      }
    );
    window.recaptchaVerifier.render().then((widgetId) => {
      window.recaptchaWidgetId = widgetId;
    });
  },
};
</script>
