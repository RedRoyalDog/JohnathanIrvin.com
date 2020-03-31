<template lang="pug">
    Section#contact.flex: b-container
        h2.text-center.h1 Contact
        FormContact
</template>

<script>
import Section from './Section';
import FormContact from './FormContact';

export default {
  name: 'TheSectionContact',
  components: {
    Section,
    FormContact,
  },
};
</script>

<style scoped>
    .flex {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
