<template lang="pug">
    Section#about
      b-container.content
        h2.h1.text-center.p-2 About
        p Johnathan Irvin is a Senior Software Engineer with over
          | 15 years of experience dreaming, designing, and building
          | complex enterprise software systems.
        p Using his knowledge as a Senior Software Engineer, Johnathan
          | provided technical expertise to the gaming journalist community.
        p After years of helping others; Johnathan planned, designed,
          | and built a community of his own --
          a(href="https://IGamePress.com") IGamePress
        p When Johnathan is not working in Cyber Security or
          | video game journalism, Johnathan makes time for contracts
          | in various industries. Such as, but not limited to
          | manufacturing, finance, trade, and more.
          a(href="#contact") Contact Now To Discuss Your Project.
</template>

<script>
import Section from './Section';
export default {
  name: 'TheSectionAbout',
  components: {
    Section,
  },
};
</script>

<style scoped>
    #about, #about .container, #about p, #about h2 {
        position: relative;
        z-index: 2;
    }

    #about p {
      font-size: 32px;
      font-weight: 400;
      line-height: 1.5;
    }
</style>
