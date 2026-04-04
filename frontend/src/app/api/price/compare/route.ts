import { proxyPricingRequest } from "@/lib/backend-proxy";

export async function POST(request: Request) {
  return proxyPricingRequest(request, "/price/compare");
}
