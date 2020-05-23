<template>
  <v-container>
    <v-layout row wrap>
      <v-flex>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field v-model="username" label="User Name" required></v-text-field>
          <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>

          <v-text-field v-model="phonenumber" :rules="phoneRules" label="Phone Number" required></v-text-field>

          <v-text-field
            v-model="password"
            :rules="passwordRules"
            label="Password"
            required
            :append-icon="passwordShow ? 'visibility' : 'visibility_off'"
            :type="passwordShow ? 'text' : 'password'"
            @click:append="passwordShow = !passwordShow"
          ></v-text-field>

          <v-text-field
            v-model="confirmPassword"
            label="Confirm Password"
            :rules="passwordRules"
            required
            :append-icon="confirmPasswordShow ? 'visibility' : 'visibility_off'"
            :type="confirmPasswordShow ? 'text' : 'password'"
            @click:append="confirmPasswordShow = !confirmPasswordShow"
          ></v-text-field>

          <v-btn :disabled="!valid" class="mx-2" color="success" @click="validate">Sign Up</v-btn>

          <v-btn color="error" class="mx-2" @click="reset">Reset Fields</v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import cryptico from "cryptico";

export default {
  data: () => ({
    passwordShow: false,
    confirmPasswordShow: false,
    valid: true,
    username: "",
    phonenumber: "",
    email: "",
    phoneRules: [
      v => !!v || "Phone Number is required",
      v => /.+351.+/.test(v) || "Phone number must be valid (+351 ...)"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    password: "",
    confirmPassword: "",
    passwordRules: [v => !!v || "Password and Confirm password Required"],
    links1: [
      {
        id: 1,
        text: "Raspy64",
        page: "/"
      }
    ]
  }),
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.registerWithFirebase();
      }
    },
    async registerWithFirebase() {
      const RSAkeys = cryptico.generateRSAKey("WeLoveInacio", 1024);
      const pk = cryptico.publicKeyString(RSAkeys);
      const user = {
        email: this.email,
        password: this.password,
        phonenumber: this.phonenumber,
        username: this.username
      };

      await this.$store.dispatch("signUpAction", user);

      var cipherusername = cryptico.encrypt(user.username, pk);
      var cipherrasp = cryptico.encrypt(1, pk);
      var cipherrasptimer = 0;
      var cipheremail = cryptico.encrypt(user.email, pk);
      var cipherphone = cryptico.encrypt(user.phonenumber, pk);
      const regist = {
        email: cipheremail.cipher,
        rasp: cipherrasp.cipher,
        rasptimer: cipherrasptimer,
        phone: cipherphone.cipher,
        username: cipherusername.cipher
      };
      if (this.$store.state.status == "success")
        await this.$store.dispatch("writeUserData", regist);
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>
