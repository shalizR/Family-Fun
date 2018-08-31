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

<style lang="scss" scoped>
  .button {
    background-color: #ffaf24;
    border-color: #ffaf24;
    color: white;
    &:hover {
      color: white;
    }
  }
</style>
