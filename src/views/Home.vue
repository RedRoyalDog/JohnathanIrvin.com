<template lang="pug">
  div
    TheHero
    TheNavBar
    TheSkillList
</template>

<script>
import TheHero from "../components/TheHero";
import TheSkillList from "../components/TheSkillList";
import  TheNavBar from "../components/TheNavBar";

export default {
  name: "Home",
  components: {
    TheHero,
    TheSkillList,
    TheNavBar
  }
};
</script>
