import Vue from "vue";
import Vuex from "vuex";
import * as firebase from "firebase";
import api from "../api/api";

Vue.use(Vuex);

const apiRoot = "http://localhost:8000";

export default new Vuex.Store({
  state: {
    user: null,
    userinfo: [],
    status: null,
    error: null,
    apierror: null,
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
    removeUser(state) {
      state.user = null;
    },
    setStatus(state, payload) {
      state.status = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
    GET_USER: function(state, response) {
      console.log(state.userinfo);
      state.userinfo = response.body;
    },
    POST_USER: function(state, response) {
      state.userinfo.push(response.body);
    },
    // Note that we added one more for logging out errors.
    API_FAIL: function(state, error) {
      console.error(error);
      if (error.url == "http://127.0.0.1:8000/") {
        state.apierror = error;
      }
    },
  },
  actions: {
    async get_user(store, uid) {
      return await api
        .get(apiRoot + "/getuser/" + uid + "/")
        .then((response) => store.commit("GET_USER", response))
        .catch((error) => store.commit("API_FAIL", error));
    },
    async post_user(store, uid, dict) {
      console.log(dict);
      return await api
        .post(apiRoot + "/postuser/" + uid + "/", dict)
        .then((response) => store.commit("POST_USER", response))
        .catch((error) => store.commit("API_FAIL", error));
    },
    async signUpAction({ commit }, payload) {
      commit("setStatus", "loading");
      firebase
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
    async signInAction({ commit }, payload) {
      console.log(await this.$store.dispatch("get_user", this.state.user));
      firebase
        .auth()
        .signInWithEmailAndPassword(payload.email, payload.password)
        .then((response) => {
          commit("setUser", response.user.uid);
          commit("setError", null);
          commit("setStatus", "success");
          return true;
        })
        .catch((error) => {
          commit("setError", error.message);
          commit("setStatus", "failure");
        });
    },
    signOutAction({ commit }) {
      firebase
        .auth()
        .signOut()
        .then(() => {
          commit("setUser", null);
          commit("setStatus", "success");
          commit("setError", null);
        })
        .catch((error) => {
          commit("setStatus", "failure");
          commit("setError", error.message);
        });
    },
  },
  getters: {
    status(state) {
      return state.status;
    },
    user(state) {
      return state.user;
    },
    error(state) {
      return state.error;
    },
  },

  modules: {},
});
