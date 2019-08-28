<template lang="pug">
    Section#contact: b-container.flex
        FormContact
</template>

<script>
import FormContact from "./FormContact";
import Section from "./Section";

export default {
    name: "TheSectionContact",
    components: {
        FormContact,
        Section
    }
};
</script>

<style scoped>
    .flex {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
