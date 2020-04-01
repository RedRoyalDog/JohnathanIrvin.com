<template lang="pug">
  div
    TheHero
    TheSectionAbout
    TheSectionSkills
    TheSectionContact
</template>

<script>
import TheHero from '../components/TheHero';
import TheSectionAbout from '../components/TheSectionAbout';
import TheSectionContact from '../components/TheSectionContact';
import TheSectionSkills from '../components/TheSectionSkills';

export default {
  name: 'Home',
  components: {
    TheHero,
    TheSectionAbout,
    TheSectionContact,
    TheSectionSkills,
  },
};
</script>
