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

          <v-text-field
            v-model="confirmPassword"
            label="Confirm Password"
            :rules="passwordRules"
            required
            :append-icon="confirmPasswordShow ? 'visibility' : 'visibility_off'"
            :type="confirmPasswordShow ? 'text' : 'password'"
            @click:append="confirmPasswordShow = !confirmPasswordShow"
          ></v-text-field>

          <v-btn
            :disabled="!valid"
            class="mx-2"
            color="success"
            @click="validate"
          >
            Register
          </v-btn>

          <v-btn color="error" class="mx-2" @click="reset">
            Reset Fields
          </v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import * as firebase from "firebase";

export default {
  data: () => ({
    passwordShow: false,
    confirmPasswordShow: false,
    valid: true,
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
    ],
    password: "",
    confirmPassword: "",
    passwordRules: [(v) => !!v || "Password and Confirm password Required"],
  }),
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.registerWithFirebase();
      }
    },
    registerWithFirebase() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then((response) => {
          alert("success");
          console.log(response);
        })
        .catch((error) => {
          alert("failure");
          console.log(error);
        });
    },
    reset() {
      this.$refs.form.reset();
    },
  },
};
</script>
