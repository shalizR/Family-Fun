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
    background-color: #ffaf24;
    border-color: #ffaf24;
    color: white;
  }
</style>
