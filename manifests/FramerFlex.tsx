import React, { useEffect, useMemo, useImperativeHandle, useRef } from "react";
import { motion, useAnimationControls } from "framer-motion";

const FramerFlex = React.forwardRef<
	HTMLDivElement,
	{
		children: React.ReactNode[];
		styles: React.CSSProperties;
		custom: {
			initialTop?: number;
			initialLeft?: number;
			initialRight?: number;
			initialBottom?: number;
			finalTop?: number;
			finalLeft?: number;
			finalRight?: number;
			finalBottom?: number;
			initialOpacity?: number;
			finalOpacity?: number;
			threshold?: number;
			hoverBackgroundColor?: string;
			hoverColor?: string;
			duration?: string;
		};
		className?: string;
	}
>((props, ref) => {
	const internalRef = useRef<HTMLDivElement>(null);

	// animation
	const controls = useAnimationControls();
	const variations = {
		initial: {
			opacity: props.custom.initialOpacity ?? 0,
			top: props.custom.initialTop || 32,
			left: props.custom.initialLeft,
			right: props.custom.initialRight,
			bottom: props.custom.initialBottom,
		},
		inView: {
			opacity: props.custom.finalOpacity ?? 1,
			top: props.custom.finalTop || 0,
			left: props.custom.finalLeft,
			right: props.custom.finalRight,
			bottom: props.custom.finalBottom,
			transition: { duration: props.custom.duration },
		},
		whileHover: {
			backgroundColor: props.custom.hoverBackgroundColor,
			color: props.custom.hoverColor,
		},
	};

	const observer = useMemo(() => {
		if (typeof window !== "undefined") {
			return new IntersectionObserver(
				(entries) => {
					entries.forEach((entry) => {
						if (entry.isIntersecting) {
							// animation start
							controls.start("inView");
						}
					});
				},
				{ threshold: props.custom.threshold ?? 0.4 }
			);
		}
	}, [controls, props.custom.threshold]);

	useEffect(() => {
		if (internalRef && internalRef.current && observer !== undefined) {
			observer.observe(internalRef.current);
		}
	}, []);

	// @ts-ignore
	useImperativeHandle(ref, () => {
		return internalRef.current;
	});

	return (
		<motion.div
			ref={internalRef}
			className={props.className}
			style={{ ...props.styles, display: "flex", position: "relative" }}
			variants={variations}
			initial="initial"
			animate={controls}
			whileHover={"whileHover"}
		>
			{props.children}
		</motion.div>
	);
});

export default FramerFlex;
