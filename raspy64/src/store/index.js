import Vue from "vue";
import Vuex from "vuex";
import * as firebase from "firebase";
import api from "../api/api";
import cryptojs from "crypto-js";
import cryptico from "cryptico";
import random from "random";

Vue.use(Vuex);

const apiRoot = "http://localhost:8000";

export default new Vuex.Store({
  state: {
    user: null,
    timeleft: 0,
    status: null,
    statusEmail: null,
    finalarr: [],
    firstcom: [],
    error: null,
    userloggedIn: null,
    usertimer: 0,
    userphone: null,
  },
  mutations: {
    setTimeLeft(state, payload) {
      state.timeleft = payload;
    },
    setUser(state, payload) {
      state.user = payload;
    },
    setUserPhone(state, payload) {
      state.userphone = payload;
    },
    setUserLoggedIn(state, payload) {
      state.userloggedIn = payload;
    },
    setTimer(state, payload) {
      state.usertimer = payload;
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
    firstcomm(state, payload) {
      state.firstcom = payload;
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
    async setTimer({ commit }, payload) {
      console.log(payload);
      commit("setTimer", payload);
    },
    async timeleft({ commit }) {
      var d = new Date();
      var rntimer = d.getHours() * 60 + d.getMinutes();
      var timer = rntimer - this.state.usertimer;
      commit("setTimeLeft", 60 - timer);
    },
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
          alert(error.message);
          commit("setError", error.message);
          commit("setStatus", "failure");
        });
    },
    async writeUserData({ commit }, payload) {
      await firebase
        .database()
        .ref("Users/" + this.state.user)
        .set({
          username: payload.username,
          raspadinha: payload.rasp,
          timerraspadinha: payload.rasptimer,
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
          console.log(response.user.uid);
          commit("setUser", response.user.uid);
          commit("setStatus", "success");
          commit("setError", null);
          commit("setStatusEmail", "success");
          alert("success on email");
        })
        .catch((error) => {
          commit("setError", error.message);
          commit("setStatus", "failure");
          alert("failure on email");
        });
    },
    updateloggedIn({ commit }) {
      commit("setUserLoggedIn", "success");
    },
    async signOutAction({ commit }) {
      const RSAkeys = cryptico.generateRSAKey("WeLoveInacio", 1024);
      const pk = cryptico.publicKeyString(RSAkeys);
      console.log("time left" + this.state.timeleft);
      if (this.state.timeleft <= 0) {
        await firebase
          .database()
          .ref("Users/" + this.state.user)
          .update({
            raspadinha: cryptico.encrypt(1, pk).cipher,
            timerraspadinha: cryptico.encrypt("0", pk).cipher,
          });
        commit("setStatus", "success");
        alert("You have one try saved");
      } else {
        var t = (60 - this.state.timeleft).toString();
        await firebase
          .database()
          .ref("Users/" + this.state.user)
          .update({
            raspadinha: cryptico.encrypt(0, pk).cipher,
            timerraspadinha: cryptico.encrypt(t, pk).cipher,
          });
        commit("setStatus", "success");
        alert("Timer Updated");
      }

      await firebase
        .auth()
        .signOut()
        .then(() => {
          commit("setUser", null);
          commit("setStatus", "success");
          commit("setError", null);
          commit("setUserLoggedIn", null);
          alert("Bye, see you next time!");
        })
        .catch((error) => {
          commit("setStatus", "failure");
          commit("setError", error.message);
          alert("Something went wrong?!");
        });
    },
    async getrasp({ commit }) {
      await api
        .get(apiRoot + "/firstcomm/")
        .then((response) => commit("firstcomm", response))
        .catch((error) => commit("API_FAIL", error));

      const obj = JSON.parse(JSON.stringify(this.state.firstcom));
      console.log(obj);
      const hmac = obj.body["hmac"];

      const hash = cryptojs.HmacSHA256(
        obj.body["msg"],
        "OneLoveInacio".toString("ascii")
      );
      const hashInBase64 = cryptojs.enc.Base64.stringify(hash);
      console.log(hmac);
      console.log(hashInBase64);
      if (hmac == hashInBase64) {
        const n = Math.floor(Math.random() * 1);
        console.log(n);
        const array = JSON.parse(atob(obj.body["msg"]));
        console.log(array);
        console.log(array[n]);
        if (array[n] == 1) {
          return true;
        } else return false;
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
