<template>
  <v-container fluid>
    <v-row>
      <v-col></v-col>
      <v-col>
        <p class="text-center headline font-weight-bold">
          Try your luck and click in the button below!
        </p>
        <v-col align="center">
          <v-dialog v-model="dialog" persistent width="550">
            <template v-slot:activator="{ on }">
              <div v-if="!userloggedIn">
                <v-btn class="w3-hover-white" v-on="on" disabled
                  >Lets win fake money!</v-btn
                >
              </div>

              <div v-else>
                <v-btn class="w3-hover-white" v-on="on" @click="getrasp()"
                  >Lets win fake money!</v-btn
                >
              </div>
            </template>
            <div v-if="!letsroll">
              <v-card>
                <v-card-title class="headline orange darken-1" primary-title
                  >Sorry!</v-card-title
                >

                <v-card-text
                  >Not yet you still have to wait
                  {{ this.$store.state.timeleft }}.</v-card-text
                >
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="orange"
                    text
                    @click="(dialog = false), aud3.play()"
                    >Okey okey!</v-btn
                  >
                </v-card-actions>
              </v-card>
            </div>
            <div v-else>
              <div v-if="victorious">
                <v-card>
                  <v-card-title class="headline orange darken-1" primary-title
                    >You Actually WON something!!!</v-card-title
                  >

                  <v-card-text>
                    <v-img
                      src="../../../public/img/icons/happy-dog.gif"
                      lazy-src
                      contain
                    ></v-img>
                  </v-card-text>
                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="orange" text @click="dialog = false"
                      >Thanks Man!</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </div>
              <div v-else>
                <v-card>
                  <v-card-title class="headline orange darken-1" primary-title
                    >Better luck next time!</v-card-title
                  >

                  <v-card-text>
                    <v-img
                      src="../../../public/img/icons/africacoffin.gif"
                      lazy-src
                      contain
                    ></v-img>
                  </v-card-text>
                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="orange" text @click="dialog = false"
                      >Never Surrender!</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </div>
            </div>
          </v-dialog>
        </v-col>
        <v-img
          src="../../../public/img/icons/take-my-money.gif"
          style="width:700px"
        >
          <div class="fill-height bottom-gradient"></div>
        </v-img>
        <v-alert type="warning">
          <h5 class>Warning!</h5>
          <h6 class="w3-opacity">
            This might be click bait continue at your own risk.
          </h6>
        </v-alert>
      </v-col>
      <v-col></v-col>
    </v-row>
  </v-container>
</template>

<script>
import cryptico from "cryptico";
import * as firebase from "firebase";
export default {
  name: "raspadinha",
  data() {
    return {
      victorious: false,
      dialog: false,
      aud1: new Audio(require("../../../public/audio/dundundun.mp3")),
      aud3: new Audio(require("../../../public/audio/yara.ogg")),
      aud2: new Audio(require("../../../public/audio/africacofin.mp3")),
      letsroll: false,
    };
  },
  computed: {
    userloggedIn() {
      console.log(this.$store.getters.userloggedIn);
      return this.$store.getters.userloggedIn;
    },
  },
  components: {},
  methods: {
    async getrasp() {
      var raspadinha;
      const RSAkeys = cryptico.generateRSAKey("WeLoveInacio", 1024);
      const pk = cryptico.publicKeyString(RSAkeys);
      await firebase
        .database()
        .ref("/Users/" + this.$store.state.user)
        .once("value")
        .then(function(snapshot) {
          raspadinha = cryptico.decrypt(
            snapshot.val() && snapshot.val().raspadinha,
            RSAkeys
          ).plaintext;
        });
      console.log(Math.floor(raspadinha));
      if (raspadinha == 0) {
        var d = new Date();
        console.log(
          d.getHours() +
            ":" +
            d.getMinutes() +
            "=" +
            (d.getHours() * 60 + d.getMinutes())
        );
        var rntimer = d.getHours() * 60 + d.getMinutes();
        console.log(this.$store.state.usertimer);
        var timer = rntimer - this.$store.state.usertimer;
        console.log(timer + this.$store.state.timeleft);

        if (timer >= 60) {
          this.letsroll = true;
        } else {
          alert("Not yet you still have to wait " + (60 - timer));
          this.letsroll = false;
        }
      } else if (raspadinha == 1) {
        await firebase
          .database()
          .ref("Users/" + this.$store.state.user)
          .update({
            raspadinha: cryptico.encrypt(0, pk).cipher,
          });
        this.letsroll = true;
      } else {
        this.letsroll = false;
      }
      this.letsroll = true;
      const val = await this.$store.dispatch("getrasp");
      this.victorious = val;
      if (this.victorious && this.letsroll) {
        //this.aud1.play();
        await this.$store.dispatch(
          "setTimer",
          d.getHours() * 60 + d.getMinutes()
        );
      } else if (!this.victorious && this.letsroll) {
        // this.aud2.play();
        await this.$store.dispatch(
          "setTimer",
          d.getHours() * 60 + d.getMinutes()
        );
      }
    },
  },
  mounted() {},
};
</script>
