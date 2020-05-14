<template>
  <v-app>
    <v-content>
      <navbarnolog />
    </v-content>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
//import navbar from "./components/mainpage/navbarlog";
import navbarnolog from "./components/mainpage/navbarnolog";

export default {
  name: "App",

  components: {
    navbarnolog,
  },

  data: () => ({
    //
  }),
};
</script>
