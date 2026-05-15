"use client";
import { motion } from "framer-motion"; // Corrected import from motion/react to framer-motion
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import * as z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema } from "@/lib/validation/schema";
import { useRouter } from "next/navigation";
import toast from "react-hot-toast";
import { useForm } from "react-hook-form";
import Link from "next/link";
import Image from "next/image";

const Login = () => {
  const router = useRouter();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<z.infer<typeof loginSchema>>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const onSubmit = async (data: z.infer<typeof loginSchema>) => {
    try {
      const url = new URL("/api/login", window.location.origin);
      url.searchParams.append("email", data.email);
      url.searchParams.append("password", data.password);

      const result = await fetch(url.toString(), {
        method: "GET",
        cache: "no-store",
      });

      const response = await result.json();
      if (result.ok) {
        toast.success(response.message);
        reset();
        router.replace("/");
      } else {
        toast.error(response.message);
      }
    } catch (err) {
      console.error("Login error:", err);
      toast.error("An error occurred. Please try again.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-gray-50 to-gray-100 p-4 sm:p-8">
      <div className="w-full max-w-5xl flex flex-col md:flex-row items-center justify-between gap-8">
        {/* Form Section */}
        <motion.div
          className="w-full md:w-1/2 flex flex-col items-center text-center space-y-6 bg-white p-8 rounded-3xl shadow-lg"
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <h1 className="text-4xl font-bold text-gray-800">Welcome Back 👋</h1>
          <p className="text-gray-500">Please enter your login details</p>
          <form
            onSubmit={handleSubmit(onSubmit)}
            className="w-full max-w-sm space-y-4"
          >
            <div>
              <Input
                {...register("email")}
                placeholder="Enter your email"
                className="w-full rounded-full border-gray-300 focus:ring-2 focus:ring-blue-500"
                type="email"
                required
              />
              {errors.email && (
                <p className="text-red-500 text-sm mt-1 text-left">
                  {errors.email.message}
                </p>
              )}
            </div>
            <div>
              <Input
                {...register("password")}
                placeholder="Enter your password"
                className="w-full rounded-full border-gray-300 focus:ring-2 focus:ring-blue-500"
                type="password"
                required
              />
              {errors.password && (
                <p className="text-red-500 text-sm mt-1 text-left">
                  {errors.password.message}
                </p>
              )}
            </div>
            <div className="flex justify-end">
              <Link
                href="/forgot-password"
                className="text-sm text-gray-400 hover:text-blue-500 transition-colors"
              >
                Forgot password?
              </Link>
            </div>
            <Button
              type="submit"
              className="w-full rounded-full bg-blue-600 hover:bg-blue-700 text-white py-2"
            >
              Log In
            </Button>
            <p className="text-sm text-gray-500">
              Don&apos;t have an account?{" "}
              <Link
                href="/signup"
                className="text-blue-600 hover:underline font-medium"
              >
                Sign Up
              </Link>
            </p>
          </form>
        </motion.div>

        {/* Image Section */}
        <motion.div
          className="w-full md:w-1/2 flex justify-center"
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <Image
            src="/ai4.jpg"
            alt="Login illustration"
            width={500}
            height={500}
            className="rounded-3xl object-cover hidden md:block"
          />
        </motion.div>
      </div>
    </div>
  );
};

export default Login;
