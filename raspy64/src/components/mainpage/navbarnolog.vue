<template>
  <v-app-bar color="orange accent-4" dense colapse-on-scroll>
    <router-link v-for="routes in links" v-bind:key="routes.id" :to="`${routes.page}`">
      <v-icon class="mx-2">home</v-icon>
    </router-link>

    <v-toolbar-title>Raspy64</v-toolbar-title>

    <v-spacer></v-spacer>
    <div v-if="!userLogedIn">
      <v-btn class="mx-2">
        <router-link
          v-for="routes in links1"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        >{{ routes.title }}</router-link>
      </v-btn>
      <v-btn class="mx-2">
        <router-link
          v-for="routes in links2"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        >{{ routes.title }}</router-link>
      </v-btn>
    </div>
    <div v-else>
      <v-btn class="mx-2" dark color="orange darken-2" @click="snackbar = true">
        <v-icon>notifications_active</v-icon>
      </v-btn>

      <v-btn class="mx-2" @click="logoutFromFirebase()">Log Out</v-btn>
    </div>
    <div>
      <v-snackbar v-model="snackbar" :timeout="timeout">
        <div v-if="checkrasp()">It's time to try ur luck!</div>
        <div v-else>U still gotta wait more {{timer}} seconds...</div>
        <v-btn color="blue" text @click="snackbar = false">Close</v-btn>
      </v-snackbar>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: "Nav",
  data: function() {
    return {
      text: "It's time to try your luck!",
      snackbar: false,
      timer: "122",
      links: [
        {
          id: 1,
          text: "Raspy64",
          page: "/"
        }
      ],
      links1: [
        {
          id: 2,
          title: "Log In",
          page: "/login"
        }
      ],
      links2: [
        {
          id: 3,
          title: "Sign Up",
          page: "/signup"
        }
      ]
    };
  },
  computed: {
    userLogedIn() {
      return this.$store.getters.user;
    }
  },
  methods: {
    logoutFromFirebase() {
      this.$store.dispatch("signOutAction");
    },
    checkrasp() {
      return false;
    }
  }
};
</script>
