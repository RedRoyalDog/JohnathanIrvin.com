<template lang="pug">
    Section#skills.flex
            h2.text-center.pt-2.h1 Skills
            i.devicon-babel-plain
</template>

<script>
import Section from './Section';

export default {
  name: 'TheSectionSkills',
  components: {
    Section,
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
