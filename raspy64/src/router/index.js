import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import signup from "../components/registo/signup.vue";
import login from "../components/login/login.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/signup",
    name: "Signup",
    component: signup,
  },
  {
    path: "/login",
    name: "LogIn",
    component: login,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
