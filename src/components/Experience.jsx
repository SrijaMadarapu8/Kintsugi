import { OrbitControls } from "@react-three/drei";
import { Avatar } from "./Avatar";
import { useThree } from "@react-three/fiber";
import { useEffect } from "react";
import { Vector3 } from "three";

export const Experience = () => {
  const { camera } = useThree();
  
  useEffect(() => {
    camera.position.set(1, 0, 5);
  }, [camera]);

  return (
    <>
      <OrbitControls 
        enablePan={false}
        enableZoom={false}
        enableRotate={false}
      />
      <group position={[2, -1, 0]}>
        <Avatar />
      </group>
      <ambientLight intensity={1} />
    </>
  );
};