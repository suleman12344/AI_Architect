"use client";
import { motion } from "framer-motion";
import Image from "next/image";
import * as z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { registerSchema } from "@/lib/validation/schema";
import { useRouter } from "next/navigation";
import toast from "react-hot-toast";
import { useForm } from "react-hook-form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Link from "next/link";

const SignUp = () => {
  const router = useRouter();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<z.infer<typeof registerSchema>>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      FirstName: "",
      LastName: "",
      email: "",
      password: "",
      fullname: "",
    },
  });

  const onSubmit = async (data: z.infer<typeof registerSchema>) => {
    try {
      const result = await fetch("/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
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
      console.error("SignUp error:", err);
      toast.error("An error occurred. Please try again.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-gray-50 to-gray-100 p-4 sm:p-8">
      <div className="w-full max-w-5xl flex flex-col md:flex-row items-center justify-between gap-8">
        {/* Image Section */}
        <motion.div
          className="w-full md:w-1/2 flex justify-center"
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <Image
            src="/ai5.png"
            alt="Sign up illustration"
            width={500}
            height={500}
            className="rounded-3xl object-cover hidden md:block"
          />
        </motion.div>

        {/* Form Section */}
        <motion.div
          className="w-full md:w-1/2 flex flex-col items-center text-center space-y-6 bg-white p-8 rounded-3xl shadow-lg"
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <h1 className="text-4xl font-bold text-gray-800">Create Account</h1>
          <p className="text-gray-500 uppercase text-sm font-semibold">
            Start for free
          </p>
          <p className="text-sm text-gray-500">
            Already a member?{" "}
            <Link
              href="/login"
              className="text-blue-600 hover:underline font-medium"
            >
              Log In
            </Link>
          </p>
          <form
            onSubmit={handleSubmit(onSubmit)}
            className="w-full max-w-sm space-y-4"
          >
            <div className="flex gap-4">
              <div className="w-1/2">
                <Input
                  {...register("FirstName")}
                  placeholder="First name"
                  className="w-full rounded-full border-gray-300 focus:ring-2 focus:ring-blue-500"
                  required
                />
                {errors.FirstName && (
                  <p className="text-red-500 text-sm mt-1 text-left">
                    {errors.FirstName.message}
                  </p>
                )}
              </div>
              <div className="w-1/2">
                <Input
                  {...register("LastName")}
                  placeholder="Last name"
                  className="w-full rounded-full border-gray-300 focus:ring-2 focus:ring-blue-500"
                  required
                />
                {errors.LastName && (
                  <p className="text-red-500 text-sm mt-1 text-left">
                    {errors.LastName.message}
                  </p>
                )}
              </div>
            </div>
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
            <div>
              <Input
                {...register("fullname")}
                placeholder="Enter your full name"
                className="w-full rounded-full border-gray-300 focus:ring-2 focus:ring-blue-500"
                required
              />
              {errors.fullname && (
                <p className="text-red-500 text-sm mt-1 text-left">
                  {errors.fullname.message}
                </p>
              )}
            </div>
            <Button
              type="submit"
              className="w-full rounded-full bg-blue-600 hover:bg-blue-700 text-white py-2"
            >
              Create Account
            </Button>
          </form>
        </motion.div>
      </div>
    </div>
  );
};

export default SignUp;
