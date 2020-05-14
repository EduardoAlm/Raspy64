<template>
  <v-app-bar color="orange accent-4" dense colapse-on-scroll>
    <router-link
      v-for="routes in links"
      v-bind:key="routes.id"
      :to="`${routes.page}`"
    >
      <v-icon class="mx-2">home</v-icon>
    </router-link>

    <v-toolbar-title>
      Raspy64
    </v-toolbar-title>

    <v-spacer></v-spacer>
    <v-btn class="mx-2">
      <router-link
        v-for="routes in links1"
        v-bind:key="routes.id"
        :to="`${routes.page}`"
      >
        {{ routes.title }}
      </router-link>
    </v-btn>
    <v-btn class="mx-2">
      <router-link
        v-for="routes in links2"
        v-bind:key="routes.id"
        :to="`${routes.page}`"
      >
        {{ routes.title }}
      </router-link>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "Nav",
  data: function() {
    return {
      links: [
        {
          id: 1,
          text: "Raspy64",
          page: "/",
        },
      ],
      links1: [
        {
          id: 2,
          title: "Log In",
          page: "/login",
        },
      ],
      links2: [
        {
          id: 3,
          title: "Sign Up",
          page: "/signup",
        },
      ],
    };
  },
};
</script>
