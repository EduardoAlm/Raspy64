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
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Nav",
  data: function() {
    return {
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
          text: "Log In",
          page: "/login",
        },
        {
          id: 3,
          text: "Sign In",
          page: "/signin",
        },
      ],
    };
  },
};
</script>
