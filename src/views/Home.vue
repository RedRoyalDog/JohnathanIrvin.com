<template lang="pug">
  div
    TheHero
    TheNavBar
</template>

<script>
import TheHero from "../components/TheHero";
import TheNavBar from "../components/TheNavBar";

export default {
  name: "Home",
  components: {
    TheHero,
    TheNavBar
  }
};
</script>
