<template lang="pug">
  div
    TheHero
    TheNavBar
    TheSectionSkills
    TheSectionAbout
    TheSectionContact
</template>

<script>
import TheHero from "../components/TheHero";
import  TheNavBar from "../components/TheNavBar";
import TheSectionAbout from "../components/TheSectionAbout";
import TheSectionContact from "../components/TheSectionContact";
import TheSectionSkills from "../components/TheSectionSkills";

export default {
  name: "Home",
  components: {
    TheHero,
    TheNavBar,

    TheSectionAbout,
    TheSectionContact,
    TheSectionSkills
  }
};
</script>
