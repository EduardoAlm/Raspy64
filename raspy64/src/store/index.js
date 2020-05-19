import Vue from "vue";
import Vuex from "vuex";
import * as firebase from "firebase";
//import api from "../api/api";

Vue.use(Vuex);

//const apiRoot = "http://localhost:8000";

export default new Vuex.Store({
  state: {
    user: null,

    status: null,
    statusEmail: null,

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
