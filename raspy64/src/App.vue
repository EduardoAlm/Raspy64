<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
  </div>
</template>


<script>
import Navlogged from "./components/mainpage/navbarlog.vue";
import Navnotlogged from "./components/mainpage/navbarnolog.vue";
import * as Cookies from "js-cookie";

export default {
  name: "app",
  data() {
    return {
      loggedIn: 0
    };
  },
  mounted() {
    this.loggedIn = Cookies.get("loggedIn");
  },
  components: {
    Navlogged: Navlogged,
    Navnotlogged: Navnotlogged
  }
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
