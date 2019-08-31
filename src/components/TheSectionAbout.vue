<template lang="pug">
    Section#about(dark)
      b-container.content
        h2.h1.text-center.p-2 About
        p Johnathan Irvin is a Senior Software Engineer with over 
          | 15 years of experience dreaming, designing, and building
          | complex enterprise software systems.
        p Using his knowledge as a Senior Software Engineer, Johnathan 
          | provided technical expertise to the gaming journalist community.
        p After years of helping others; Johnathan planned, designed,
          | and built a community of his own -- 
          a(href="https://IGamePress.com").bg-black IGamePress
        p When Johnathan is not working in Cyber Security or 
          | video game journalism, Johnathan makes time for contracts 
          | in various industries. Such as, but not limited to 
          | manufacturing, finance, trade, and more. 
          a(href="#contact").bg-black Contact Now To Discuss Your Project.
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

    #about::after {
        content: "";
        background: url(../assets/img2.jpg) no-repeat center center;
        background-size: cover;
        background-attachment: fixed;
        opacity: 0.45;

        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        position: absolute;
        z-index: 1;
    }

    #about .content {
      /* Permalink - use to edit and share this gradient: https://colorzilla.com/gradient-editor/#000000+0,000000+70,000000+100&0.75+0,0.75+22,0.5+42,0+70,0+100 */
      background: -moz-radial-gradient(center, ellipse cover,  rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.75) 22%, rgba(0,0,0,0.5) 42%, rgba(0,0,0,0) 70%, rgba(0,0,0,0) 100%); /* FF3.6-15 */
      background: -webkit-radial-gradient(center, ellipse cover,  rgba(0,0,0,0.75) 0%,rgba(0,0,0,0.75) 22%,rgba(0,0,0,0.5) 42%,rgba(0,0,0,0) 70%,rgba(0,0,0,0) 100%); /* Chrome10-25,Safari5.1-6 */
      background: radial-gradient(ellipse at center,  rgba(0,0,0,0.75) 0%,rgba(0,0,0,0.75) 22%,rgba(0,0,0,0.5) 42%,rgba(0,0,0,0) 70%,rgba(0,0,0,0) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
      filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#bf000000', endColorstr='#00000000',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
    }

    .bg-black {
      background-color: #000;
    }
</style>
