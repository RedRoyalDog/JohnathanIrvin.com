<template lang="pug">
    Section#about(dark)
        p About
</template>

<script>
import  Section from "./Section";
export default {
    name: "TheSectionAbout",
    components: {
        Section,
    },
};
</script>

<style scoped>
    #about {
        position: relative;
        z-index: 2;
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
</style>