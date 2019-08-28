<template lang="pug">
    section.navSection(
        :class="{ 'bg-dark': dark, 'text-light': dark }"
    )
        b-container(fluid)
            slot
</template>

<script>
export default {
    name: "Section",
    props: {
        dark: {
            type: Boolean,
            default: false,
            required: false
        }
    }
};
</script>

<style scoped>
.navSection {
    min-height: 100%;  /* Fallback for browsers do NOT support vh unit */
    min-height: 100vh;
    padding-bottom: 56px;
}
</style>
