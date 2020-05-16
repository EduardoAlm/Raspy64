import Vue from "vue";
import Vuex from "vuex";
import * as firebase from "firebase";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    status: null,
    error: null,
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
  },
  actions: {
    signUpAction({ commit }, payload) {
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
    signInAction({ commit }, payload) {
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
