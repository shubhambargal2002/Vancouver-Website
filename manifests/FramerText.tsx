import React, { useCallback } from "react";
import { motion, useAnimationControls } from "framer-motion";

const FramerText = React.forwardRef<
	HTMLDivElement,
	{
        styles: React.CSSProperties;
		custom: {
            text?: string;
			hoverColor?: string;
			nonHoverColor?: string;
			height?: number;
			duration?: number;
		};
        className?: string;
	}
>((props, ref) => {
	const textVariants = {
		mouseleave: { color: props.custom.nonHoverColor || "#000000" },
		mouseenter: {
			color: props.custom.hoverColor || "#c4c4c4",
		},
	};
	const underlineVariants = {
		mouseleave: {
			backgroundColor: props.custom.nonHoverColor || "#000000",
			transition: { duration: props.custom.duration ?? 2 },
			width: "0%",
		},
		mouseenter: {
			backgroundColor: props.custom.hoverColor || "#c4c4c4",
			transition: { duration: props.custom.duration ?? 2 },
			width: "100%",
		},
	};
	const controls = useAnimationControls();
	const onMouseEnter = useCallback((e: React.MouseEvent) => {
		controls.start("mouseenter");
	}, []);
	const onMouseLeave = useCallback((e: React.MouseEvent) => {
		controls.start("mouseleave");
	}, []);
	return (
		<div ref={ref} className={props.className} style={props.styles} onMouseEnter={onMouseEnter} onMouseLeave={onMouseLeave}>
			<motion.div
				animate={controls}
				variants={textVariants}
				initial={"mouseleave"}
			>
				{props.custom.text}
			</motion.div>
			<motion.div
				animate={controls}
				variants={underlineVariants}
				initial={"mouseleave"}
				style={{ height: `${props.custom.height}px` ?? "2px" }}
			></motion.div>
		</div>
	);
});

export default FramerText;