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
    background-color: #e28a2b;
    border-color: #e28a2b;
    color: white;
  }
</style>
