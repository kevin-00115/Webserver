<template>
    <div>text info</div>
    
</template>

<script>
export default {
    emits: ['routeSwitch'],
    created() {
        this.$emit('routeSwitch', this.$route)
    }
}
</script>

<style>

</style>