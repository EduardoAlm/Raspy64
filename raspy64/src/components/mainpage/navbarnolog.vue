<template>
  <v-app-bar color="orange accent-4" dense colapse-on-scroll>
    <router-link v-for="routes in links" v-bind:key="routes.id" :to="`${routes.page}`">
      <v-icon class="mx-2">home</v-icon>
    </router-link>

    <v-toolbar-title>Raspy64</v-toolbar-title>

    <v-spacer></v-spacer>
    <div v-if="!userloggedIn">
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
      <v-btn class="mx-2" dark color="orange darken-2" @click="snackbar = true;checkrasp()">
        <v-icon>notifications_active</v-icon>
      </v-btn>

      <v-btn class="mx-2" @click="logoutFromFirebase()">Log Out</v-btn>
    </div>
    <div>
      <v-snackbar v-model="snackbar" :timeout="2000">
        <div v-if="isAvail">It's time to try ur luck!</div>
        <div v-else>U still gotta wait {{ timer }} minutes.</div>
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
      timer: this.$store.state.timeleft,
      isAvail: false,
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
    userloggedIn() {
      return this.$store.getters.userloggedIn;
    }
  },
  methods: {
    logoutFromFirebase() {
      this.$store.dispatch("signOutAction");
    },
    async checkrasp() {
      await this.$store.dispatch("timeleft");
      if (this.$store.state.timeleft > 0) {
        this.timer = this.$store.state.timeleft;
        this.isAvail = false;
      } else {
        this.isAvail = true;
      }
    }
  }
};
</script>
