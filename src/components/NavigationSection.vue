<template lang="pug">
    section.navSection
        slot
</template>

<script>
export default {
    name: "NavigationSection"
};
</script>

<style scoped>
.navSection {
    height: 100vh;
}
</style>
