<template>
  <button @click="$emit('click')" class="button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'Button',
}
</script>

<style scoped>
  .button {
    background-color: white;
    /*border-color: white;*/
    color: black;
  }
</style>
