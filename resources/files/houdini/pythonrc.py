#<custom_edits> : Commented this section to deactivate prism initiation on start up
'''
# >>>PrismStart
try:
    import PrismInit

    PrismInit.createPrismCore()
except Exception as e:
    print(str(e))
# <<<PrismEnd
'''
#</custom_edits>