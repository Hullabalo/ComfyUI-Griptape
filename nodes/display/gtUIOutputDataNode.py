class gtUIOutputDataNode:
    NAME = "Griptape Display: Data"
    DESCRIPTION = "Display output data."
    CATEGORY = "Griptape/Display"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}, "optional": {"INPUT": ("*", {"forceInput": True})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("OUTPUT",)
    FUNCTION = "func"
    OUTPUT_NODE = True

    def func(self, INPUT=None):
        if INPUT:
            return {
                "ui": {"INPUT": str(INPUT)},  # UI message for the frontend
                "result": (str(INPUT),),
            }
        else:
            return {
                "ui": {"INPUT": ""},
                "result": ("",),
            }

        # The latest updates to Comfy seem to have broken the node. 
        # Using validate_input as described in the documentation (https://docs.comfy.org/essentials/custom_node_more_on_inputs) 
        # resolves the issue for JSON inputs (CONFIG and MEMORY).
        # TODO For more complex objects (AGENT, RULESETS, TOOLS), it remains to be seen what has changed in the ComfyUI code for ui.
        @classmethod
        def VALIDATE_INPUTS(s, input_types):
            return True

