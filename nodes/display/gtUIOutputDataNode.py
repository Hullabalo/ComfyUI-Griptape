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

    # resolve no output (at least for me) for CONFIG and MEMORY - must have a look at ComfyUI code to see what changed (security) for STRING input type
    # non-json type AGENT, RULESETS and TOOLS does'nt work atm 
    @classmethod
    def VALIDATE_INPUTS(s, input_types):
        return True
