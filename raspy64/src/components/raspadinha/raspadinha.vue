<template>
  <v-container fluid>
    <v-row>
      <v-col></v-col>
      <v-col>
        <p
          class="text-center headline font-weight-bold"
        >Try your luck and click in the button below!</p>
        <v-col align="center">
          <v-dialog v-model="dialog" persistent width="550">
            <template v-slot:activator="{ on }">
              <v-btn class="w3-hover-white" v-on="on" @click="getrasp()">Lets win fake money!</v-btn>
            </template>
            <div v-if="victorious">
              <v-card>
                <v-card-title
                  class="headline orange darken-1"
                  primary-title
                >You Actually WON something!!!</v-card-title>

                <v-card-text>
                  <v-img src="../../../public/img/icons/happy-dog.gif" lazy-src contain></v-img>
                </v-card-text>
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="orange" text @click="dialog = false;aud3.play()">Thanks Man!</v-btn>
                </v-card-actions>
              </v-card>
            </div>
            <div v-else>
              <v-card>
                <v-card-title class="headline orange darken-1" primary-title>Better luck next time!</v-card-title>

                <v-card-text>
                  <v-img src="../../../public/img/icons/africacoffin.gif" lazy-src contain></v-img>
                </v-card-text>
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="orange" text @click="dialog = false">Never Surrender!</v-btn>
                </v-card-actions>
              </v-card>
            </div>
          </v-dialog>
        </v-col>
        <v-img src="../../../public/img/icons/take-my-money.gif" style="width:700px">
          <div class="fill-height bottom-gradient"></div>
        </v-img>
        <v-alert type="warning">
          <h5 class>Warning!</h5>
          <h6 class="w3-opacity">This might be click bait continue at your own risk.</h6>
        </v-alert>
      </v-col>
      <v-col></v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "raspadinha",
  data() {
    return {
      victorious: false,
      dialog: false,
      aud1: new Audio(require("../../../public/audio/dundundun.mp3")),
      aud3: new Audio(require("../../../public/audio/yara.ogg")),
      aud2: new Audio(require("../../../public/audio/africacofin.mp3"))
    };
  },
  components: {},
  methods: {
    async getrasp() {
      await this.$store.dispatch("getrasp");

      if (this.victorious) {
        this.aud1.play();
      } else {
        this.aud2.play();
      }
    }
  },
  mounted() {}
};
</script>
