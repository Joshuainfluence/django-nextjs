'use server'

import { cookies } from "next/headers"
import { NextResponse } from "next/server"

export default async function POST(request) {
    return NextResponse.json({"message" : "Hi world"}, {status:200})
}