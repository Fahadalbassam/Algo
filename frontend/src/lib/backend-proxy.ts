import "server-only";

import { NextResponse } from "next/server";

const BACKEND_API_BASE_URL = process.env.BACKEND_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function proxyPricingRequest(request: Request, path: string): Promise<NextResponse> {
  let payload: unknown;

  try {
    payload = await request.json();
  } catch {
    return NextResponse.json(
      { detail: "Invalid JSON payload sent to the frontend proxy." },
      { status: 400 },
    );
  }

  try {
    const response = await fetch(`${BACKEND_API_BASE_URL}${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      cache: "no-store",
    });

    const rawBody = await response.text();
    const contentType = response.headers.get("content-type") ?? "application/json";

    return new NextResponse(rawBody, {
      status: response.status,
      headers: {
        "Content-Type": contentType,
        "Cache-Control": "no-store",
      },
    });
  } catch {
    return NextResponse.json(
      {
        detail: `Unable to reach the FastAPI backend at ${BACKEND_API_BASE_URL}. Start the backend server or update BACKEND_API_BASE_URL.`,
      },
      { status: 502 },
    );
  }
}
