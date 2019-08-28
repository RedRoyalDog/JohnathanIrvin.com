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
    min-height: 100%;  /* Fallback for browsers do NOT support vh unit */
    min-height: calc(100vh - 56px);
}
</style>
