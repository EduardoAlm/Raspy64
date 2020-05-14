<template>
  <v-container fluid>
    <v-row>
      <v-col></v-col>
      <v-col>
        <p class="text-center headline font-weight-bold">
          Try your luck and click in the button below!
        </p>
        <v-col align="center">
          <v-btn class="w3-hover-white">Lets win fake money!</v-btn>
        </v-col>
        <v-img
          src="../../../public/img/icons/take-my-money.gif"
          style="width:700px"
          ><div class="fill-height bottom-gradient"></div
        ></v-img>
        <v-alert type="warning">
          <h5 class="">Warning!</h5>
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
export default {
  name: "raspadinha",
  data() {
    return {};
  },
  components: {},
  methods: {},
  mounted() {},
};
</script>
