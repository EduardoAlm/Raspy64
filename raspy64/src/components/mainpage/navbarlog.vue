<template>
  <div class="w3-container w3-panel w3-leftbar w3-border-gray">
    <nav class="w3-section w3-bar w3-black">
      <div class="w3-left">
        <router-link
          class="w3-btn w3-wide"
          v-for="routes in links"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        >
          <img
            v-if="routes.imageUrl"
            :src="routes.imageUrl"
            style="width: 80px; height: 40px;"
          />
          {{ routes.text }}
        </router-link>
      </div>
      <div class="w3-right">
        <router-link
          class="w3-button w3-wide w3-white w3-block"
          v-for="routes in links1"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        >
          {{ routes.text }}
        </router-link>
        <router-link v-bind:key="link.id" :to="`${link.page}`">
          <button
            :id="logout"
            class="w3-button w3-red w3-hover-opacity w3-margin-left"
            style="font-family: sans-serif, letter-spacing: 3px"
            @click="logout"
          >
            Terminar Sessão
          </button>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script>
import * as Cookies from "js-cookie";

export default {
  name: "Nav2",
  data: function() {
    return {
      link: {
        id: 1,
        text: "Raspy64",
        page: "/",
      },
      links: [
        {
          id: 0,
          page: "/",
          imageUrl: require("../../../public/img/icons/logo.png"),
        },
      ],
      links1: [
        {
          id: 2,
          text: Cookies.get("loggedName"),
          page: "/mainUser",
        },
      ],
    };
  },
  methods: {
    logout() {
      Cookies.set("loggedIn", 0);
      Cookies.remove("loggedName");
      Cookies.set("stop", false);
    },
  },
};
</script>
