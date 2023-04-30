import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "FramerText",
    styles : {
        boxShadowOptions: true,
        flexContainerOptions: false,
        flexChildOptions: true,
        positionOptions: true,
        typographyOptions: true,
        spacingOptions: true,
        sizeOptions: true,
        borderOptions: true,
        outlineOptions: true,
        backgroundOptions: true,
        miscellaneousOptions: true,
      },

	custom: {
        text: {type: 'text'},
		hoverColor: { type: "color" },
		nonHoverColor: { type: "color" },
		height: { type: "number" },
		duration: { type: "number" },
	},
});