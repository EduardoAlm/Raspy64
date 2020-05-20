import Vue from "vue";
import Vuex from "vuex";
import * as firebase from "firebase";
import api from "../api/api";
//import cryptojs from "crypto-js";

Vue.use(Vuex);
//import cryptico from "cryptico";
const apiRoot = "http://localhost:8000";

export default new Vuex.Store({
  state: {
    user: null,

    status: null,
    statusEmail: null,
    finalarr: [],
    error: null,
    userloggedIn: null,

    userphone: null,
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
    setUserPhone(state, payload) {
      state.userphone = payload;
    },
    setUserLoggedIn(state, payload) {
      state.userloggedIn = payload;
    },
    setSMSResult(state, payload) {
      state.smsresult = payload;
    },
    removeUser(state) {
      state.user = null;
    },
    setStatus(state, payload) {
      state.status = payload;
    },
    setStatusSMS(state, payload) {
      state.statusSMS = payload;
    },
    setStatusEmail(state, payload) {
      state.statusEmail = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },

    get_finalarr(state, payload) {
      state.finalarr = payload;
    },
    API_FAIL: function(state, error) {
      console.error(error);
      if (error.url == "http://localhost:8000/") {
        state.error = error;
      }
    },
  },
  actions: {
    async signUpAction({ commit }, payload) {
      commit("setStatus", "loading");
      await firebase
        .auth()
        .createUserWithEmailAndPassword(payload.email, payload.password)
        .then((response) => {
          alert("success");
          commit("setUser", response.user.uid);
          commit("setError", null);
          commit("setStatus", "success");
        })
        .catch((error) => {
          commit("setError", error.message);
          commit("setStatus", "failure");
        });
    },
    async writeUserData({ commit }, payload) {
      firebase
        .database()
        .ref("Users/" + this.state.user)
        .set({
          username: payload.username,
          raspadinha: payload.rasp,
          email: payload.email,
          phonenumber: payload.phone,
        });
      commit("setStatus", "success");
    },

    async signInActionEmail({ commit }, payload) {
      //console.log(this.$store.dispatch("get_user", this.state.user));
      return await firebase
        .auth()
        .signInWithEmailAndPassword(payload.email, payload.password)
        .then((response) => {
          commit("setUser", response.user.uid);
          commit("setStatus", "success");
          commit("setError", null);
          commit("setStatusEmail", "success");
          console.log("success");
        })
        .catch((error) => {
          commit("setError", error.message);
          commit("setStatus", "failure");
        });
    },
    updateloggedIn({ commit }) {
      commit("setUserLoggedIn", "success");
    },
    async signOutAction({ commit }) {
      await firebase
        .auth()
        .signOut()
        .then(() => {
          commit("setUser", null);
          commit("setStatus", "success");
          commit("setError", null);
          commit("setUserLoggedIn", null);
          alert("Bye");
        })
        .catch((error) => {
          commit("setStatus", "failure");
          commit("setError", error.message);
          alert("Something went wrong?!");
        });
    },
    async getrasp({ commit }) {
      await api
        .get(apiRoot + "/getfinalarr/")
        .then((response) => commit("get_finalarr", response))
        .catch((error) => commit("API_FAIL", error));

      console.log(this.state.finalarr.body);
      const rr = atob(this.state.finalarr.body);

      const array = JSON.parse(rr);
      console.log(array);
      const n = Math.floor(Math.random() * 9 + 0);
      console.log(n);
      console.log(array[n]);
      if (array[n] == 1) {
        return true;
      } else return false;
    },
  },
  getters: {
    status(state) {
      return state.status;
    },
    userloggedIn(state) {
      return state.userloggedIn;
    },
    error(state) {
      return state.error;
    },
  },

  modules: {},
});
