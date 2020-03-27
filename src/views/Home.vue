<template lang="pug">
  div
    TheNavBar
    TheHero
    TheSectionAbout
    TheSectionSkills
    TheSectionContact
</template>

<script>
import TheHero from '../components/TheHero';
import TheNavBar from '../components/TheNavBar';
import TheSectionAbout from '../components/TheSectionAbout';
import TheSectionContact from '../components/TheSectionContact';
import TheSectionSkills from '../components/TheSectionSkills';
import CanvasParticleVue from '../components/CanvasParticle.vue';

export default {
  name: 'Home',
  components: {
    TheHero,
    TheNavBar,

    TheSectionAbout,
    TheSectionContact,
    TheSectionSkills,
  },
};
</script>
