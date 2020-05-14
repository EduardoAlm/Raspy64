<template>
  <div>
    <mainpage></mainpage>
  </div>
</template>

<script>
import mainpage from "../components/mainpage/mainpage.vue";
import * as Cookies from "js-cookie";
export default {
  name: "Home",
  components: {
    mainpage
  },
  mounted() {
    console.log(Cookies.get("stop"));
    if (Cookies.get("stop") === "false") {
      window.location.reload(true);
      Cookies.set("stop", true);
      console.log(Cookies.get("stop"));
    }
  }
};
</script>
