<template lang="pug">
    section.navSection
        slot
</template>

<script>
export default {
    name: "SectionNavigation"
};
</script>

<style scoped>
.navSection {
    height: 100vh;
}
</style>
