import FramerFlex from "./FramerFlex";
import React from "react";

const DevFramerFlex: typeof FramerFlex =
	React.forwardRef((props, ref) => {
		const overrideStyles =
			props.children.length === 0
				? {
						height: "100px",
						border: "1px dashed black",
                        width: "100%"
				  }
				: props.styles;
		return (
			<FramerFlex
				ref={ref}
				{...props}
				styles={overrideStyles}
			/>
		);
	});

export default DevFramerFlex;