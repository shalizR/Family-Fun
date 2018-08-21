<template>
  <button @click="$emit('click')" class="button is-rounded is-large">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'Button'
}
</script>

<style scoped>
  .button {
    background-color: white;
    border-color: black;
    color: black;
  }
</style>
