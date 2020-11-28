<script>
  import Modal from "svelte-simple-modal";
  import Content from "./Content.svelte";

  export let isOpen;
  export let message;

  const styleBg = { background: "lightgray" };
  const styleContent = { background: "lightgray", textAlign: "center" };
</script>

{#if isOpen}
  <Modal
    {styleBg}
    {styleContent}
    closeButton={false}
    closeOnEsc={false}
    closeOnOuterClick={false}>
    <Content {message} />
  </Modal>
{/if}
